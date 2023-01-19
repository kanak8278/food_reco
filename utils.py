"""### Augmentation Visualization"""

class FoodDataset(Dataset):
  def __init__(self, path_list, transforms=None):
    self.path_list = path_list
    self.transforms = transforms
  
  def __len__(self):
    return len(self.path_list)
  
  def __getitem__(self, idx):
    path = self.path_list[idx]
    img = Image.open(path).convert('RGB') 
    
    img = np.array(img)
    label = cls2idx[os.path.dirname(self.path_list[idx]).split('/')[-1]] #label from the parent folder
    img = img.reshape(img.shape[0], img.shape[1], -1)
    
    if self.transforms is not None:
      img = self.transforms(image=img)["image"] #apply transforms
    return img, label



def visualize_augmentations(dataset, idx=0, samples=10, cols=5, random_img = True):
    
    dataset = copy.deepcopy(dataset)
    print(A.Compose([t for t in dataset.transforms if not isinstance(t, (A.Normalize, ToTensorV2))]))
    
    dataset.transforms = A.Compose([t for t in dataset.transforms if not isinstance(t, (A.Normalize, ToTensorV2))])
    rows = samples // cols
    
        
    figure, ax = plt.subplots(nrows=rows, ncols=cols, figsize=(72, 48))
    for i in range(samples):
        if random_img:
            idx = np.random.randint(1,len(dataset))
        image, lab = dataset[idx]
        ax.ravel()[i].imshow(image)
        ax.ravel()[i].set_axis_off()
        ax.ravel()[i].set_title(lab)
    plt.tight_layout(pad=1)
    plt.show()


