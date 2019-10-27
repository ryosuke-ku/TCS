	public Boolean hexists(final String key, final String field) {
		return pipeline.hexists(key, field).get();
	}
