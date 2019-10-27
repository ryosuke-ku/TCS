	public Long hincrBy(final String key, final String field, final long value) {
		return pipeline.hincrBy(key, field, value).get();
	}
