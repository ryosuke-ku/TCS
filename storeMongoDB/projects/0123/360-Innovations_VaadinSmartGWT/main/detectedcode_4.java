	public HandlerRegistration addSelectionChangedHandler(final SelectionChangedHandler handler) {
		selectionChangedHandlers.add(handler);
		return new HandlerRegistration() {
			@Override
			public void removeHandler() {
				selectionChangedHandlers.remove(handler);
			}
		};
	}
