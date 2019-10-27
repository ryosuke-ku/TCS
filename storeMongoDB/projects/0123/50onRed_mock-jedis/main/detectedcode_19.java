	public Long hdel(final String key, final String... fields) {
		return pipeline.hdel(key, fields).get();
	}
