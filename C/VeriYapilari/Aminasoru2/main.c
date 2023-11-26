    #include <stdio.h>
    #include <stdlib.h>
    #include<string.h>

    struct cell {
        char *anahtar;
        struct cell *next;
    };

    struct table_node{
        int count;
        struct cell *header;
    };

    struct hash_tablosu{
        struct table_node *tablo_basi;
        int tablo_uzunlugu;
        int multiplier;
    };

    unsigned int hash(char *s, int multiplier, int table_size){
        int i=0;
        unsigned int value =0;
        while(s[i] != '\0'){
            value=(s[i]+multiplier*value) % table_size;
            i++;
        }
        return value;
    }


    void sirali_listeye_ekle (struct cell **liste_basi, char *icerik) {
        struct cell* newnode = (struct cell*)malloc(sizeof(struct cell)); //init
        struct cell* iter = *liste_basi;
        newnode->anahtar=icerik;
        newnode->next=NULL;

        if(*liste_basi==NULL){
            *liste_basi=newnode;
        }
        else if (icerik < (*liste_basi)->anahtar){
            newnode->next = *liste_basi;
            *liste_basi=newnode;
        }
        else {
            while (iter->next != NULL && iter->next->anahtar < icerik)
                iter=iter->next;
            if (iter->next !=NULL && iter->next->anahtar == icerik) // ayni degeri ikinci kere eklemeni engelliyor
                return;                                             // eger iter son node a kadar geldiyse eklenecek sayi diger hepsinden buyuk demek
            newnode->next = iter->next;
            iter->next=newnode;
        }
    }

    void listeyi_hash_tablosuna_donusturme(struct hash_tablosu *htable, struct cell **liste_basi){

        struct cell* iter = *liste_basi;

        while (iter != NULL){
            struct cell *l = (htable->tablo_basi+hash(iter->anahtar, htable->multiplier,htable->tablo_uzunlugu))->header;

            if (!l ){
                l = iter;
                (htable->tablo_basi+hash(iter->anahtar,htable->multiplier,htable->tablo_uzunlugu))->count++;
            }
            else{

                while (strcmp(iter->anahtar, l->anahtar)){
                    l = l->next;
                }
                l = iter;
                (htable->tablo_basi+hash(iter->anahtar,htable->multiplier,htable->tablo_uzunlugu))->count++;
            }
            iter=iter->next;
        }

        return;

    }


void listeyi_hash_tablosuna_donusturme4(struct hash_tablosu *htable, struct cell **liste_basi){

	while((*liste_basi) != NULL)
    {
        int hash_index = hash((*liste_basi)->anahtar, htable->multiplier, htable->tablo_uzunlugu);
        struct cell *temp= (*liste_basi)->next;
        (*liste_basi)->next = NULL;

        if((htable->tablo_basi+hash_index)->header == NULL){
            (htable->tablo_basi+hash_index)->header = *liste_basi;
            (htable->tablo_basi+hash_index)->count++;
        }
        else{
            struct cell *iter = NULL;
            iter = (htable->tablo_basi+hash_index)->header;

            while(iter!=NULL){
                if(strcmp((*liste_basi)->anahtar,iter->anahtar)) {
                    if(iter->next!=NULL) {
                        iter=iter->next;
                    }
                    else{
                        iter->next = *liste_basi;
                        (htable->tablo_basi+hash_index)->count++;
                    }
                }
                else{
                    break;
                }
            }
        }
        *liste_basi = temp;
    }



}

    void initialize_hash_table1(struct hash_tablosu **hash_table,int multiplier,int tablo_uzunlugu){
        int i;

        *hash_table=(struct hash_tablosu*)malloc(sizeof(struct hash_tablosu));
       // *hash_table = (struct table_node*)malloc(TABLE_SIZE*sizeof(struct table_node));
        if(*hash_table==NULL){
            printf("Hash hablosu icin gerekli yer ayrilamadi. Hata...");
            exit(1);
        }
        (*hash_table)->tablo_basi = (struct table_node*)malloc(tablo_uzunlugu*sizeof(struct table_node));
        if((*hash_table)->tablo_basi==NULL){
            printf("Hash hablosu icin gerekli yer ayrilamadi. Hata...");
            exit(1);
        }
        (*hash_table)->tablo_uzunlugu = tablo_uzunlugu;
        (*hash_table)->multiplier = multiplier;

        for(i=0; i<tablo_uzunlugu; i++){
            (((*hash_table)->tablo_basi)+i)->count=0;
           (((*hash_table)->tablo_basi)+i)->header=NULL;
        }
    }


    void print_list(struct cell *l){
        if(l!=NULL){
            printf("%s ",l->anahtar);
            print_list(l->next);
        }
    }


    void hash_table_print1(struct hash_tablosu *hash_table){
        if(hash_table!=NULL){
            int i;
            printf("---- Hash Table icerigi----\n");
            for(i=0; i<hash_table->tablo_uzunlugu; i++){
                printf("%5d : (%2d) ",i,(hash_table->tablo_basi+i)->count);
                print_list((hash_table->tablo_basi+i)->header);
                printf("\n");
            }
        }
        else printf("\nHash table bos...\n");
    }
    void print_hash_table(struct hash_tablosu *hash_table){
    if(hash_table){
        int index;
        printf("----- HASH TABLOSU -----\n");
        for(index=0; index<hash_table->tablo_uzunlugu; index++){
            printf("%5d : (%2d) ",index,(hash_table->tablo_basi +index)->count);
          //  printf("%5d : (%2d) ",index,hash_table->tablo_basi[index].counter);
            print_list((hash_table->tablo_basi+index)->header);
            printf("\n");
        }
    }
    else printf("Hash Tablosu Bos ...\n");

}
void liste_yok_et(struct cell **liste_basi){
    struct cell *onceki;
    while(*liste_basi){
        onceki=*liste_basi;
        *liste_basi=(*liste_basi)->next;
        free(onceki->anahtar);
        free(onceki);
    }
}
    int main()
    {

        struct cell *root=NULL;

        sirali_listeye_ekle(&root,"kadayif");
        sirali_listeye_ekle(&root,"Trabzonspor");
        sirali_listeye_ekle(&root,"gundogdu");
        sirali_listeye_ekle(&root,"besiktas");
        sirali_listeye_ekle(&root,"baklava");
        sirali_listeye_ekle(&root,"dembaba");
        sirali_listeye_ekle(&root,"cardoza");
        sirali_listeye_ekle(&root,"besiktas");
        sirali_listeye_ekle(&root,"bakiray");
        sirali_listeye_ekle(&root,"beklava");
        sirali_listeye_ekle(&root,"beklavaa");
        sirali_listeye_ekle(&root,"beklavas");
        sirali_listeye_ekle(&root,"beklavasd");
        print_list(root);
        printf("\n");

        struct hash_tablosu* htable = NULL;
        initialize_hash_table1(&htable,3,5);

        listeyi_hash_tablosuna_donusturme4(htable, &root);
        //hash_table_print1(htable);
        print_hash_table(htable);

        //printf("%s", htable->tablo_basi->header->anahtar);
        return 0;
    }
