	public void dispose()
	{
		T valueModel = getValueModel();

		if (valueModel != null)
		{
			valueModel.removeCollectionChangeListener(collectionChangeHandler);
		}
	}
