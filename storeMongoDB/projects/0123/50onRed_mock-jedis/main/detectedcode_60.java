	public byte[] lpop(final byte[] key) {
		return pipeline.lpop(key).get();
	}
