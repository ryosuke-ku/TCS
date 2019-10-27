	public Boolean exists(final byte[] key) {
		return pipeline.exists(key).get();
	}
