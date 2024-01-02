import streamlit as st


def write_main_help():
    st.write('This is the main help page and will eventually contain actual help.')


def main():
    st.title('Marta strikes back!')
    st.write('This is a front end for our NWSL fantasy league.')

    # add help button
    st.button("Help", on_click=st.help, args=(write_main_help,))
    st.sidebar.success('Please select mode above!')


if __name__ == "__main__":
    main()
