	public Long sort(final byte[] key, final SortingParams sortingParameters, final byte[] dstkey) {
		return pipeline.sort(key, sortingParameters, dstkey).get();
	}
