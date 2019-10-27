	public List<String> hvals(final String key) {
		return pipeline.hvals(key).get();
	}
