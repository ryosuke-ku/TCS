	public Set<String> hkeys(final String key) {
		return pipeline.hkeys(key).get();
	}
