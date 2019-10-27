	public Long hset(final String key, final String field, final String value) {
		return pipeline.hset(key, field, value).get();
	}
