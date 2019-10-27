	protected boolean checkIfOperationIsSavePoint(UndoRedoOperation peekLast)
	{
		for (SavePoint savePoint : getSavePoints())
		{
			if (peekLast.equals(savePoint.getOrigin()))
			{
				return true;
			}
		}

		return false;
	}
