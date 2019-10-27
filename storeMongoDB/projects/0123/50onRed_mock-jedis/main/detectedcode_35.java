	public Long incr(final String key) {
		return pipeline.incr(key).get();
	}
