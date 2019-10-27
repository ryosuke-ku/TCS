	public Set<byte[]> smembers(final byte[] key) {
		return pipeline.smembers(key).get();
	}
