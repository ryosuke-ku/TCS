	public List<byte[]> lrange(final byte[] key, final long start, final long end) {
		return pipeline.lrange(key, start, end).get();
	}
