import streamlit as st
import requests
import json
from datetime import datetime

# API base URL
API_BASE_URL = "http://127.0.0.1:8000"

# Initialize session state
if 'token' not in st.session_state:
    st.session_state.token = None
if 'username' not in st.session_state:
    st.session_state.username = None

# Helper functions
def login_user(username, password):
    """Login user and get access token"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/token",
            data={"username": username, "password": password},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        if response.status_code == 200:
            token_data = response.json()
            st.session_state.token = token_data["access_token"]
            st.session_state.username = username
            return True, "Login successful!"
        else:
            error_msg = response.json().get("detail", "Login failed")
            return False, error_msg
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {str(e)}"

def register_user(username, password):
    """Register new user"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/register",
            params={"username": username, "password": password}
        )
        if response.status_code == 200:
            return True, "Registration successful! You can now login."
        else:
            error_msg = response.json().get("detail", "Registration failed")
            return False, error_msg
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {str(e)}"

def get_headers():
    """Get authorization headers"""
    if st.session_state.token:
        return {"Authorization": f"Bearer {st.session_state.token}"}
    return {}

def create_note(title, content):
    """Create a new note"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/notes",
            json={"title": title, "content": content},
            headers=get_headers()
        )
        if response.status_code == 200:
            return True, "Note created successfully!"
        else:
            error_msg = response.json().get("detail", "Failed to create note")
            return False, error_msg
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {str(e)}"

def get_notes():
    """Get all user notes"""
    try:
        response = requests.get(
            f"{API_BASE_URL}/notes",
            headers=get_headers()
        )
        if response.status_code == 200:
            return True, response.json()
        else:
            error_msg = response.json().get("detail", "Failed to fetch notes")
            return False, error_msg
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {str(e)}"

def get_note(note_id):
    """Get specific note"""
    try:
        response = requests.get(
            f"{API_BASE_URL}/notes/{note_id}",
            headers=get_headers()
        )
        if response.status_code == 200:
            return True, response.json()
        else:
            error_msg = response.json().get("detail", "Note not found")
            return False, error_msg
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {str(e)}"

def delete_note(note_id):
    """Delete a note"""
    try:
        response = requests.delete(
            f"{API_BASE_URL}/notes/{note_id}",
            headers=get_headers()
        )
        if response.status_code == 200:
            return True, "Note deleted successfully!"
        else:
            error_msg = response.json().get("detail", "Failed to delete note")
            return False, error_msg
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {str(e)}"

def update_note(note_id, title, content):
    """Update a note"""
    try:
        response = requests.put(
            f"{API_BASE_URL}/notes/{note_id}",
            json={"title": title, "content": content},
            headers=get_headers()
        )
        if response.status_code == 200:
            return True, "Note updated successfully!"
        else:
            error_msg = response.json().get("detail", "Failed to update note")
            return False, error_msg
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {str(e)}"

def logout():
    """Logout user"""
    st.session_state.token = None
    st.session_state.username = None

# Page configuration
st.set_page_config(
    page_title="Note System",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        font-size: 2.5rem;
        margin-bottom: 2rem;
    }
    .note-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .note-title {
        font-weight: bold;
        color: #333;
        font-size: 1.2rem;
    }
    .note-content {
        color: #666;
        margin-top: 0.5rem;
    }
    .sidebar .element-container {
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">📝 Note System</h1>', unsafe_allow_html=True)

# Sidebar for navigation
with st.sidebar:
    st.header("Navigation")
    
    if st.session_state.token:
        st.success(f"Welcome, {st.session_state.username}!")
        
        menu_option = st.selectbox(
            "Choose Action",
            ["View Notes", "Create Note", "Edit Note", "Delete Note", "Search Note"]
        )
        
        if st.button("🚪 Logout", type="secondary"):
            logout()
            st.rerun()
    else:
        auth_option = st.selectbox("Choose Option", ["Login", "Register"])

# Main content area
if not st.session_state.token:
    # Authentication section
    st.markdown("---")
    
    if auth_option == "Login":
        st.subheader("🔐 Login")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            
            if st.button("🚀 Login", type="primary", use_container_width=True):
                if username and password:
                    success, message = login_user(username, password)
                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.warning("Please fill in all fields")
    
    else:  # Register
        st.subheader("📝 Register")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            new_username = st.text_input("Username", placeholder="Choose a username")
            new_password = st.text_input("Password", type="password", placeholder="Choose a password")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
            
            if st.button("✨ Register", type="primary", use_container_width=True):
                if new_username and new_password and confirm_password:
                    if new_password == confirm_password:
                        success, message = register_user(new_username, new_password)
                        if success:
                            st.success(message)
                        else:
                            st.error(message)
                    else:
                        st.error("Passwords do not match")
                else:
                    st.warning("Please fill in all fields")

else:
    # User is logged in - show main functionality
    if menu_option == "View Notes":
        st.subheader("📚 Your Notes")
        
        # Refresh button
        if st.button("🔄 Refresh Notes"):
            st.rerun()
        
        success, notes_data = get_notes()
        if success:
            if notes_data:
                # Display notes with action buttons
                for i, note in enumerate(notes_data):
                    with st.container():
                        col1, col2 = st.columns([4, 1])
                        
                        with col1:
                            st.markdown(f"""
                            <div class="note-card">
                                <div class="note-title">📌 {note['title']}</div>
                                <div class="note-content">{note['content']}</div>
                                <small style="color: #999;">Note ID: {note['id']} | Owner ID: {note['owner_id']}</small>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col2:
                            st.markdown("<br>", unsafe_allow_html=True)  # Spacing
                            if st.button(f"🗑️ Delete", key=f"delete_{note['id']}", type="secondary"):
                                success_del, message = delete_note(note['id'])
                                if success_del:
                                    st.success(message)
                                    st.rerun()
                                else:
                                    st.error(message)
                            
                            if st.button(f"✏️ Edit", key=f"edit_{note['id']}", type="secondary"):
                                st.session_state.edit_note_id = note['id']
                                st.session_state.edit_title = note['title']
                                st.session_state.edit_content = note['content']
                                st.rerun()
                    
                    st.divider()
                    
                st.info(f"Total notes: {len(notes_data)}")
            else:
                st.info("📝 No notes found. Create your first note!")
        else:
            st.error(f"Failed to load notes: {notes_data}")
    
    elif menu_option == "Create Note":
        st.subheader("✨ Create New Note")
        
        with st.form("create_note_form"):
            note_title = st.text_input("Title", placeholder="Enter note title")
            note_content = st.text_area("Content", placeholder="Write your note here...", height=200)
            
            submitted = st.form_submit_button("📝 Create Note", type="primary")
            
            if submitted:
                if note_title and note_content:
                    success, message = create_note(note_title, note_content)
                    if success:
                        st.success(message)
                        st.balloons()
                    else:
                        st.error(message)
                else:
                    st.warning("Please fill in both title and content")
    
    elif menu_option == "Edit Note":
        st.subheader("✏️ Edit Note")
        
        # Show edit form if note is selected
        if hasattr(st.session_state, 'edit_note_id') and st.session_state.edit_note_id:
            with st.form("edit_note_form"):
                st.info(f"Editing Note ID: {st.session_state.edit_note_id}")
                edited_title = st.text_input("Title", value=st.session_state.edit_title)
                edited_content = st.text_area("Content", value=st.session_state.edit_content, height=200)
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.form_submit_button("💾 Update Note", type="primary"):
                        if edited_title and edited_content:
                            success, message = update_note(st.session_state.edit_note_id, edited_title, edited_content)
                            if success:
                                st.success(message)
                                # Clear edit state
                                del st.session_state.edit_note_id
                                del st.session_state.edit_title
                                del st.session_state.edit_content
                                st.balloons()
                            else:
                                st.error(message)
                        else:
                            st.warning("Please fill in both title and content")
                
                with col2:
                    if st.form_submit_button("❌ Cancel", type="secondary"):
                        # Clear edit state
                        del st.session_state.edit_note_id
                        del st.session_state.edit_title
                        del st.session_state.edit_content
                        st.rerun()
        else:
            st.info("Select a note to edit from the 'View Notes' section, or search for a specific note ID below.")
            
            # Alternative: Enter note ID manually
            st.markdown("---")
            note_id_to_edit = st.number_input("Or enter Note ID to edit", min_value=1, step=1)
            if st.button("🔍 Load Note for Editing"):
                success, note_data = get_note(int(note_id_to_edit))
                if success:
                    st.session_state.edit_note_id = note_data['id']
                    st.session_state.edit_title = note_data['title']
                    st.session_state.edit_content = note_data['content']
                    st.rerun()
                else:
                    st.error(f"Note not found: {note_data}")
    
    elif menu_option == "Delete Note":
        st.subheader("🗑️ Delete Note")
        
        st.warning("⚠️ Note deletion is permanent and cannot be undone!")
        
        note_id_to_delete = st.number_input("Enter Note ID to delete", min_value=1, step=1)
        
        # Show note preview before deletion
        if st.button("🔍 Preview Note"):
            success, note_data = get_note(int(note_id_to_delete))
            if success:
                st.markdown(f"""
                <div class="note-card" style="border-left-color: #dc3545;">
                    <div class="note-title">📌 {note_data['title']}</div>
                    <div class="note-content">{note_data['content']}</div>
                    <small style="color: #999;">Note ID: {note_data['id']} | Owner ID: {note_data['owner_id']}</small>
                </div>
                """, unsafe_allow_html=True)
                
                st.error("⚠️ This note will be permanently deleted!")
            else:
                st.error(f"Note not found: {note_data}")
        
        # Confirmation checkbox
        confirm_delete = st.checkbox("I understand that this action cannot be undone")
        
        if st.button("🗑️ Delete Note", type="secondary", disabled=not confirm_delete):
            if confirm_delete:
                success, message = delete_note(int(note_id_to_delete))
                if success:
                    st.success(message)
                    st.balloons()
                else:
                    st.error(message)
            else:
                st.warning("Please confirm that you want to delete this note")
    
    elif menu_option == "Search Note":
        st.subheader("🔍 Search Note")
        
        note_id = st.number_input("Enter Note ID", min_value=1, step=1)
        
        if st.button("🔍 Search"):
            success, note_data = get_note(int(note_id))
            if success:
                st.markdown(f"""
                <div class="note-card">
                    <div class="note-title">📌 {note_data['title']}</div>
                    <div class="note-content">{note_data['content']}</div>
                    <small style="color: #999;">Note ID: {note_data['id']} | Owner ID: {note_data['owner_id']}</small>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error(f"Note not found: {note_data}")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>Note System GUI - Built with Streamlit</div>",
    unsafe_allow_html=True
)