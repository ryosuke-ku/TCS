	public String hget(final String key, final String field) {
		return pipeline.hget(key, field).get();
	}
