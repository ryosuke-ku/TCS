	public void rollback(SavePoint savePoint)
	{
		try
		{
			beginTransaction();

			UndoRedoOperation origin = savePoint.getOrigin();

			// Do not rollback if the origin is not in currently applied actions. e.g.: it was undone earlier.
			// origin null means there was no
			if (origin == null || getOperations().contains(origin))
			{
				Iterator<UndoRedoOperation> descendingIterator = getOperations().descendingIterator();

				LinkedList<UndoRedoOperation> undoSavePointOperations = new LinkedList<UndoRedoOperation>();

				while (descendingIterator.hasNext())
				{
					UndoRedoOperation undoRedoValueModelAction = descendingIterator.next();

					if (origin != null && undoRedoValueModelAction.equals(origin))
					{
						break;
					}

					undoSavePointOperations.addFirst(undoRedoValueModelAction);
					descendingIterator.remove();
					undoRedoValueModelAction.undo();
				}

				// No operations were undone, no need for an undo state
				if (!undoSavePointOperations.isEmpty())
				{
					SavePointUndoRedoOperation savePointUndoRedoOperation = new SavePointUndoRedoOperation(undoSavePointOperations);
					getRedoableOperations().addFirst(savePointUndoRedoOperation);
				}
			}

			getSavePoints().removeLast();
		}
		finally
		{
			endTransaction();
		}

	}
