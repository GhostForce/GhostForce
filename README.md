
NAME
    GhostForce - GhostForce abuses the small keyspace of ghostbin paste ids when considered with the population.

DESCRIPTION
    Tested on Ubuntu 14.04. The build script would need to be ported for any other distro.
    
    Install and Config:
            Master Node:
                    tar -xf ./gf.tar
                    cd GhostForce
                    ./list_gen.py
                    mkdir ../back
                    mv ./values/*.txt ../back
                    Add proxies one per line in format ip,port in proxy_list.txt
    
            Configure scanning packages:
                    cp back/[filename].txt GhostForce/values/newnode.txt
                    tar -cf ./gf.tar ./GhostForce
    
            Deploy Node:
                    tar -xf ./gf.tar
                    cd GhostForce
                    sudo ./build.sh
                    ./GhostForce.py
    
            Alternativally the scanning nodes need the following packages:
                    python-dev 
                    build-essential
                    python-lxml
                    python-bs4

FUNCTIONS
    worker(id)
        worker(id) 
                Takes the id to be tested and will either add an entry to duds.txt or validurls.txt. If a valid id 
                is found the contents are saved to a file named <id>.txt
        Functions local to worker()
                get_page(id)
                        Takes a page id and attempts to return the raw html for that url. A random proxy is used to bypass 
                        rate limiting.
                find_code(raw)
                        Takes the raw html, parses out the user input from the paste.


NAME
    list_gen - Used to create the id files for scanning nodes. The keyspace is 32^5 in size, or roughly 30,000,000 items.

DESCRIPTION
    Usage:
            ./list_gen.py
    
    The list generation will take a while, up to 2 min on some machines.
    
    You will be prompted to enter the number of nodes you wish to run. All files will be placed 
            in ./values/[0th element].txt

FUNCTIONS
    build_list()
        build_list() returns a list of all the possible configurations of the character set for ghostbin paste ids.

NAME
    my_pool

CLASSES
    __builtin__.object
        Pool
    
    class Pool(__builtin__.object)
     |  Very basic process pool with timeout.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, size=None, timeout=15)
     |      Create new `Pool` of `size` concurrent processes.
     |      
     |      Args:
     |          size (int): Number of concurrent processes. Defaults to
     |              no. of processors.
     |          timeout (int, optional): Number of seconds to wait before
     |              killing the process.
     |  
     |  map(self, func, it)
     |      Call `func` with each element in iterator `it`.
     |      
     |      Args:
     |          func (callable): Function/method to call.
     |          it (TYPE): List of arguments to pass to each call of `func`.
     |      
     |      Returns:
     |          list: The results of all the calls to `func`.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)


AUTHOR
    GhostForce[at]mailinator.com
