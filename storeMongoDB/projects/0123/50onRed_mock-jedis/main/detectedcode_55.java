	public Boolean sismember(final byte[] key, final byte[] member) {
		return pipeline.sismember(key, member).get();
	}
