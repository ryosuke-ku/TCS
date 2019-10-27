	public void paintContent(PaintTarget target) throws PaintException {
		propertyPainter.paintContent(target);

		if (dataSource != null) {
			target.addAttribute("dataSource", dataSource);
		}

		if (!selectionChangedHandlers.isEmpty()) {
			target.addAttribute("*hasSelectionChangedHandlers", true);
		}

		if (!selectionUpdatedHandlers.isEmpty()) {
			target.addAttribute("*hasSelectionUpdatedHandlers", true);
		}

		if (!recordDoubleClickHandlers.isEmpty()) {
			target.addAttribute("*hasRecordDoubleClickHandlers", true);
		}

		super.paintContent(target);
	}
