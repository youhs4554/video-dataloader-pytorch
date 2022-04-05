from video_dataloader_pytorch.data_loader.data_loaders import VideoDataLoader
import pytest

@pytest.fixture
def train_loader():
    train_loader, _ = init_data()
    return train_loader

def init_data():
    data_dir = "/data/FallDownData/FDD"
    batch_size = 8
    fold = 1
    sample_length = 10
    num_workers = 4
    
    train_loader, valid_loader = None, None
    
    try:
        train_loader = VideoDataLoader(
                data_dir, batch_size=batch_size, fold=fold,
                sample_length=sample_length,
                validation_split=0.05, num_workers=num_workers)
        valid_loader = train_loader.split_validation()
    except:
        pass
    
    return train_loader, valid_loader

def test_init_data(train_loader):
    assert train_loader is not None
    
def test_data_batch(train_loader):
    train_loader_iter = iter(train_loader)
    train_batch = next(train_loader_iter)
    print("\nType of batch", train_batch.keys())
    print("Clip shape(s)", train_batch['clip'].shape)
    print("Label shape(s)", train_batch['label'].shape)
    assert train_loader is not None