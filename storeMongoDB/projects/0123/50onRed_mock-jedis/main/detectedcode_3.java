	public Long incrBy(final String key, final long integer) {
		return pipeline.incrBy(key, integer).get();
	}
