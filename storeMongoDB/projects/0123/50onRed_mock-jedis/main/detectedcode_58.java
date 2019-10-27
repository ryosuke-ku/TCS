	public Long srem(final byte[] key, final byte[]... members) {
		return pipeline.srem(key, members).get();
	}
