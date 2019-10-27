	public void commit(SavePoint savePoint)
	{
		if (savePoint == null)
		{
			if (!getSavePoints().isEmpty())
			{
				throw new IllegalStateException("A null SavePoint was committed while there are SavePoints tracked");
			}

			return;
		}

		if (getSavePoints().isEmpty() || !getSavePoints().contains(savePoint) || !getSavePoints().peekLast().equals(savePoint))
		{
			throw new IllegalStateException("Trying to commit SavePoint that is not tracked by the UndoRedoManager");
		}

		getSavePoints().removeLast();
	}
