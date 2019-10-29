public class Canvas {

























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































	public HandlerRegistration addClickHandler(final ClickHandler handler) {
		clickHandlers.add(handler);
		return new HandlerRegistration() {
			@Override
			public void removeHandler() {
				clickHandlers.remove(handler);
			}
		};
	}




































































































































































































































































































	public void setDisabled(boolean disabled) {
		setAttribute("b$disabled", disabled);
		requestRepaint();
	}










	public boolean getDisabled() {
		Boolean disabled = getAttributeAsBoolean("b$disabled");
		return disabled == null ? false : disabled;
	}


	public boolean isEnabled() {
		return !getDisabled();
	}


	public void setEnabled(boolean enabled) {
		setDisabled(!enabled);
	}
















































































































































































	public void paintContent(PaintTarget target) throws PaintException {
		super.paintContent(target);

		if (!clickHandlers.isEmpty()) {
			target.addAttribute("*hasClickHandlers", true);
		}
	}


	public void changeVariables(Object source, Map<String, Object> variables) {
		super.changeVariables(source, variables);

		if (variables.containsKey("clickEvent")) {
			final ClickEvent event = new ClickEvent();

			for (ClickHandler handler : clickHandlers) {
				handler.onClick(event);
			}
		}
	}
}