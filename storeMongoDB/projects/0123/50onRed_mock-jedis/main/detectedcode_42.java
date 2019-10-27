	public Map<String, String> hgetAll(final String key) {
		return pipeline.hgetAll(key).get();
	}
