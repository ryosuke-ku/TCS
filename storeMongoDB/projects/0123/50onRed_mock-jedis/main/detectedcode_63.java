	public Long llen(final byte[] key) {
		return pipeline.llen(key).get();
	}
