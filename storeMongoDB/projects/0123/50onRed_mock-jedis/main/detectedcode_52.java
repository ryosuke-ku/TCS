	public Long sadd(final byte[] key, final byte[]... members) {
		return pipeline.sadd(key, members).get();
	}
