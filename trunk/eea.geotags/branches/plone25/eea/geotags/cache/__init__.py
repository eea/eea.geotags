""" Caching module
"""
try:
    from eea.cache import cache as ramcache
    from lovely.memcached.event import InvalidateCacheEvent
    ramcache, InvalidateCacheEvent
except ImportError:
    # Fail quiet if required cache packages are not installed in order to use
    # this package without caching
    from eea.geotags.cache.nocache import ramcache
    from eea.geotags.cache.nocache import InvalidateCacheEvent
    ramcache, InvalidateCacheEvent

from eea.geotags.cache.cache import cacheGeoJsonKey
cacheGeoJsonKey
