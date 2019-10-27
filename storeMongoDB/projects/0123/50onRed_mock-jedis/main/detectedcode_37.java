	public Long del(final byte[] key) {
		return pipeline.del(key).get();
	}
