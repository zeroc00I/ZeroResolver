import pymongo, multiprocessing

class output_result:
    def __init__(self,list_to_resolve):
        self.domain = domain
        self.nameserver = nameserver
        self.collection = collection
        self.client = pymongo.MongoClient("127.0.0.1", 27017)
        self.db = client.resolved
        self.db.collection.drop()
        self.collection = db['collection']
        self.list_to_resolve = list_to_resolve
        self.data_manipulation(self.domain,self.nameserver)

    def process_queue():
           parallelism = multiprocessing.Pool(options.threads)


    def data_manipulation(self,domain,nameserver):
        resolver = dns_resolver(2)
        domain,ip,dns,status = resolver.get_a_entry(domain,nameserver)

        if domain:

            domain_already_exist = len(
                list(
                    self.collection.find({
                        'HOST':domain
                    })
                )
            )
            
            print('[?] domain {} has domain_already_exist = {}'.format(domain,domain_already_exist))

            if domain_already_exist:
               print('[+] domain {} already exist on DB'.format(domain))
               self.collection.update_one(
                    {
                        "HOST":domain
                    },
                    {
                        "$push":{
                            'lookups':{
                                "IP":ip,
                                "DNS":dns,
                                "status":status
                            }
                        }
                    }
                )

            else:
                print('[-] domain {} doesnt exist on DB. Inserting... '.format(domain))

                self.collection.insert_one(
                    {
                        "HOST":domain,
                            'lookups':[{
                                "IP":ip,
                                "DNS":dns,
                                "status":status
                            }]
                    }
                )

        print('{} {}'.format(list(self.collection.find()),"\n"))
