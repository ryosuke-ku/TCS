	public Double incrByFloat(final byte[] key, final double integer) {
		return pipeline.incrByFloat(key, integer).get();
	}
