	public Long lpush(final byte[] key, final byte[]... strings) {
		return pipeline.lpush(key, strings).get();
	}
