import os


def create_proj_dir(dir_name):
    # def create_project_dir(directory):
    '''
    Check if the given folder name
    is created or not then create it
    '''
    if not os.path.exists(dir_name):
        print("creating your [ " + dir_name + " ] ......")
        os.makedirs(dir_name)
    else:
        print("You have created [ " + dir_name + " ] before")


def create_data_files(proj_name, base_url):
    '''
    Check if the (getURL.txt) and (setURL.txt)
    is created or not then create it
    '''
    queue = os.path.join(proj_name, 'getURL.txt')
    scraped = os.path.join(proj_name, 'setURL.txt')
    if not os.path.isfile(queue):
        write_to_file(queue, base_url)
    if not os.path.isfile(scraped):
        write_to_file(scraped, '')


def write_to_file(path, data):
    '''
    Write the given data to the files after deleting
    the previous data in the start of the project
    '''
    with open(path, 'w') as f:
        f.write(data)


def append_to_file(path, data):
    '''
    Write the given data to the files without deleting
    the previous data in the start of the project
    '''
    with open(path, 'a') as f:
        f.write(data, '\n')


def delete_file_data(path):
    # def delete_file_contents(path):
    '''
    clear any data in the file
    '''
    open(path, 'w').close()
    # with open(path, 'w')

# Changing the way that this scraper work to get the data
# needed for the scraping and the data written by it to
# get the start data from (getURL.txt) and add it to a
# (set) and to read from it
# then add the comming data to the (set) the write it to
# (setURL.txt)
# this will enhance the speedup of the scrapper the full thing
#  will work fine with out it but work slow


def file_to_set(file_name):
    '''
    get the all data stored in the created file
    and add them to set and read the data from it
    insted of the files it self
    '''
    result = set()
    with open(file_name, 'rt') as f:
        for line in f:
            result.add(line.replace('\n', ''))
    return result


def set_to_file(links, file_name):
    '''
    get the all data stored in the
    set and write them to the files
    '''
    with open(file_name, "w") as f:
        for link in sorted(links):
            f.write(link+"\n")
