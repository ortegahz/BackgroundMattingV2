"""
This file records the directory paths to the different datasets.
You will need to configure it for training the model.

All datasets follows the following format, where fgr and pha points to directory that contains jpg or png.
Inside the directory could be any nested formats, but fgr and pha structure must match. You can add your own
dataset to the list as long as it follows the format. 'fgr' should point to foreground images with RGB channels,
'pha' should point to alpha images with only 1 grey channel.
{
    'YOUR_DATASET': {
        'train': {
            'fgr': 'PATH_TO_IMAGES_DIR',
            'pha': 'PATH_TO_IMAGES_DIR',
        },
        'valid': {
            'fgr': 'PATH_TO_IMAGES_DIR',
            'pha': 'PATH_TO_IMAGES_DIR',
        }
    }
}
"""

DATA_PATH = {
    'videomatte240k': {
        'train': {
            'fgr': '/media/sdb/data/matting-data/VideoMatte240K_JPEG_SD/train/fgr',
            'pha': '/media/sdb/data/matting-data/VideoMatte240K_JPEG_SD/train/pha'
        },
        'valid': {
            'fgr': '/media/sdb/data/matting-data/VideoMatte240K_JPEG_SD/test/fgr',
            'pha': '/media/sdb/data/matting-data/VideoMatte240K_JPEG_SD/test/pha'
        }
    },
    'photomatte13k': {
        'train': {
            'fgr': 'PATH_TO_IMAGES_DIR',
            'pha': 'PATH_TO_IMAGES_DIR'
        },
        'valid': {
            'fgr': 'PATH_TO_IMAGES_DIR',
            'pha': 'PATH_TO_IMAGES_DIR'
        }
    },
    'distinction': {
        'train': {
            'fgr': '/media/sdb/data/matting-data/Distinctions-646/Train/FG',
            'pha': '/media/sdb/data/matting-data/Distinctions-646/Train/GT',
        },
        'valid': {
            'fgr': '/media/sdb/data/matting-data/Distinctions-646/Test/FG',
            'pha': '/media/sdb/data/matting-data/Distinctions-646/Test/GT'
        },
    },
    'adobe': {
        'train': {
            'fgr': 'PATH_TO_IMAGES_DIR',
            'pha': 'PATH_TO_IMAGES_DIR',
        },
        'valid': {
            'fgr': 'PATH_TO_IMAGES_DIR',
            'pha': 'PATH_TO_IMAGES_DIR'
        },
    },
    'backgrounds': {
        'train': '/media/sdb/data/matting-data/Backgrounds/train',
        'valid': '/media/sdb/data/matting-data/Backgrounds/valid'
    },
}