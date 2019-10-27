	public Long hlen(final String key) {
		return pipeline.hlen(key).get();
	}
