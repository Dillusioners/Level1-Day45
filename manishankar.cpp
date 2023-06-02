# include <iostream>
# include <string>

/**
 * Author: LeeTuah
 * Date: June 2nd, 2023
 * For SuperB league event
*/

// main program execution starts from here
int main(int argc, char** argv){
    // variables declared here
    std::string male_gene, female_gene, p_trait;
    int probability = 0;

    // asking user for the male gene
    std::cout << "Enter the character of the male gene (eg. TT): ";
    std::cin >> male_gene;

    // asking user for the female gene
    std::cout << "Enter the character of the female gene (eg. tt): ";
    std::cin >> female_gene;

    // asking user for the probable trate
    std::cout << "Enter the particular trait to check the probability of: ";
    std::cin >> p_trait;

    // iterating through all of the possibilities of the traits
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            // generating a new offspring trait from the two traits
            std::string offspring = std::string(1, male_gene[j]) + std::string(1, female_gene[i]);
            // if the offspring trait matches with the probable trait, add 1, else 0
            probability += (offspring == p_trait);
        }
    }

    // printing the probable trait
    std::cout << "\nThe probability of your trait is " << probability * 25 << "%";
}
