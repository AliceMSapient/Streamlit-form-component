import os
import streamlit.components.v1 as components


_RELEASE = False



if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        # "my_component",
        "my_form",
        # "my_form",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    # _component_func = components.declare_component("my_component", path=build_dir)
    _component_func = components.declare_component("my_class_form", path=build_dir)



def my_form(name, key=None):
    """Create a new instance of "my_component".

    Parameters
    ----------
    name: str
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        The number of times the component's "Click Me" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
   
    component_value = _component_func(name=name, key=key, default="the initial form")

 
    return component_value



if not _RELEASE:
    import streamlit as st




st.subheader("Hook Form Component")
return_val = my_form('alice', key="alice" token= "")
st.write(return_val)