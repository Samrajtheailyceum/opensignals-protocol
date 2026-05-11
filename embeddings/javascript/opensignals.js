/**
 * OpenSignals Protocol - JavaScript Client Library
 * Version: 0.1.0
 *
 * Easy integration for publishers and SSPs
 */

(function(global) {
  'use strict';

  const OpenSignals = {
    version: '0.1.0',
    config: {
      endpoint: null,
      apiKey: null,
      autoVerify: false,
      cacheResults: true,
      cacheTTL: 3600, // seconds
      timeout: 5000 // ms
    },
    cache: new Map(),

    /**
     * Initialize OpenSignals
     * @param {Object} options - Configuration options
     */
    init(options) {
      this.config = { ...this.config, ...options };

      if (!this.config.endpoint) {
        console.warn('OpenSignals: No endpoint specified. Using default.');
        this.config.endpoint = 'https://verify.opensignals.org/v1';
      }

      console.log('OpenSignals initialized:', this.version);
    },

    /**
     * Verify a signal
     * @param {Object} params - Verification parameters
     * @returns {Promise<Object>} Verification result
     */
    async verify(params) {
      const { signal_id, brand, market, category, intended_use = 'targeting' } = params;

      // Check cache
      if (this.config.cacheResults) {
        const cached = this._getFromCache(signal_id, brand, market, category);
        if (cached) {
          return { ...cached, cached: true };
        }
      }

      // Make API request
      try {
        const response = await this._request('/verify', {
          signal_id,
          brand,
          market,
          category,
          intended_use
        });

        // Cache result
        if (this.config.cacheResults && response.decision) {
          this._addToCache(signal_id, brand, market, category, response);
        }

        return response;
      } catch (error) {
        console.error('OpenSignals verification error:', error);
        return {
          decision: 'error',
          error: error.message,
          cached: false
        };
      }
    },

    /**
     * Batch verify multiple signals
     * @param {Array<Object>} signals - Array of signal parameters
     * @returns {Promise<Array<Object>>} Verification results
     */
    async verifyBatch(signals) {
      return Promise.all(signals.map(signal => this.verify(signal)));
    },

    /**
     * Get signal manifest
     * @param {string} signal_id - Signal identifier
     * @returns {Promise<Object>} Signal manifest
     */
    async getManifest(signal_id) {
      return this._request(`/manifest/${signal_id}`);
    },

    /**
     * Validate a manifest
     * @param {Object} manifest - Signal manifest to validate
     * @returns {Promise<Object>} Validation result
     */
    async validateManifest(manifest) {
      return this._request('/validate-manifest', manifest);
    },

    /**
     * Log signal usage for audit
     * @param {Object} params - Audit parameters
     * @returns {Promise<Object>} Audit result
     */
    async audit(params) {
      return this._request('/audit', params);
    },

    /**
     * Make API request
     * @private
     */
    async _request(endpoint, data = null) {
      const url = `${this.config.endpoint}${endpoint}`;
      const options = {
        method: data ? 'POST' : 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
        timeout: this.config.timeout
      };

      if (this.config.apiKey) {
        options.headers['Authorization'] = `Bearer ${this.config.apiKey}`;
      }

      if (data) {
        options.body = JSON.stringify(data);
      }

      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), this.config.timeout);
      options.signal = controller.signal;

      try {
        const response = await fetch(url, options);
        clearTimeout(timeoutId);

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        return await response.json();
      } catch (error) {
        clearTimeout(timeoutId);
        throw error;
      }
    },

    /**
     * Get from cache
     * @private
     */
    _getFromCache(signal_id, brand, market, category) {
      const key = `${signal_id}:${brand}:${market}:${category}`;
      const cached = this.cache.get(key);

      if (!cached) return null;

      const now = Date.now();
      if (now - cached.timestamp > this.config.cacheTTL * 1000) {
        this.cache.delete(key);
        return null;
      }

      return cached.data;
    },

    /**
     * Add to cache
     * @private
     */
    _addToCache(signal_id, brand, market, category, data) {
      const key = `${signal_id}:${brand}:${market}:${category}`;
      this.cache.set(key, {
        data,
        timestamp: Date.now()
      });

      // Limit cache size
      if (this.cache.size > 1000) {
        const firstKey = this.cache.keys().next().value;
        this.cache.delete(firstKey);
      }
    },

    /**
     * Clear cache
     */
    clearCache() {
      this.cache.clear();
    }
  };

  // Export for different module systems
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = OpenSignals;
  } else if (typeof define === 'function' && define.amd) {
    define([], function() { return OpenSignals; });
  } else {
    global.OpenSignals = OpenSignals;
  }

})(typeof window !== 'undefined' ? window : global);
