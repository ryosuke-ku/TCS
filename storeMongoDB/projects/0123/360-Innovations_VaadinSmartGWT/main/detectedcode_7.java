	public HandlerRegistration addSelectionUpdatedHandler(final SelectionUpdatedHandler handler) {
		selectionUpdatedHandlers.add(handler);
		return new HandlerRegistration() {
			@Override
			public void removeHandler() {
				selectionUpdatedHandlers.remove(handler);
			}
		};
	}
