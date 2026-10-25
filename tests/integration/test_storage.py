import pytest
from services.api.services.storage import LocalStorage

@pytest.fixture
def storage():
    return LocalStorage()

def test_store_file(storage):
    file_path = "test_file.txt"
    content = b"Hello, World!"
    
    # Store the file
    storage.store(file_path, content)
    
    # Verify the file was stored correctly
    assert storage.exists(file_path)
    assert storage.retrieve(file_path) == content

def test_retrieve_non_existent_file(storage):
    file_path = "non_existent_file.txt"
    
    # Verify that retrieving a non-existent file raises an error
    with pytest.raises(FileNotFoundError):
        storage.retrieve(file_path)

def test_delete_file(storage):
    file_path = "test_file_to_delete.txt"
    content = b"Hello, to be deleted!"
    
    # Store the file
    storage.store(file_path, content)
    
    # Delete the file
    storage.delete(file_path)
    
    # Verify the file was deleted
    assert not storage.exists(file_path)

def test_delete_non_existent_file(storage):
    file_path = "non_existent_file_to_delete.txt"
    
    # Verify that deleting a non-existent file raises an error
    with pytest.raises(FileNotFoundError):
        storage.delete(file_path)