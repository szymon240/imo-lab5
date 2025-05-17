import utils
from hae import hae
from utils import load_from_tsp

if __name__ == "__main__":
    kroa200_matrix, kroa200_coords = load_from_tsp('datasets/kroA200.tsp')
    krob200_matrix, krob200_coords = load_from_tsp('datasets/kroB200.tsp')

    kroa200_cycle1_random, kroa200_cycle2_random, _ = utils.initialize_random_cycles(kroa200_matrix)
    krob200_cycle1_random, krob200_cycle2_random, _ = utils.initialize_random_cycles(krob200_matrix)

    # Wariant z LS po rekombinacji
    best_sol_ls, best_len_ls, t_ls, iter_ls = hae(kroa200_matrix, use_local_search_after_recomb=True)
    print('HAE + LS: length=', best_len_ls, 'iter=', iter_ls)

    # Wariant bez LS po rekombinacji
    best_sol_no_ls, best_len_no_ls, t_no_ls, iter_no_ls = hae(kroa200_matrix, use_local_search_after_recomb=False)
    print('HAE no-LS: length=', best_len_no_ls, 'iter=', iter_no_ls)

    # # 2) Steepest descent (oryginalne przeszukiwanie lokalne)
    # utils.run_test_lab2(
    #     "kroA: Steepest search (original)",
    #     kroa200_matrix,
    #     kroa200_coords,
    #     kroa200_cycle1_random,
    #     kroa200_cycle2_random,
    #     local_search.steepest_original
    # )
    # utils.run_test_lab2(
    #     "kroB: Steepest search (original)",
    #     krob200_matrix,
    #     krob200_coords,
    #     krob200_cycle1_random,
    #     krob200_cycle2_random,
    #     local_search.steepest_original
    # )

    # 3) LNS: Large Neighborhood Search
    # utils.run_test_lab2(
    #     "kroA: LNS (regret repair)",
    #     kroa200_matrix,
    #     kroa200_coords,
    #     kroa200_cycle1_random,
    #     kroa200_cycle2_random,
    #     lns_wrapper
    # )
    # utils.run_test_lab2(
    #     "kroB: LNS (regret repair)",
    #     krob200_matrix,
    #     krob200_coords,
    #     krob200_cycle1_random,
    #     krob200_cycle2_random,
    #     lns_wrapper
    # )

    # utils.run_test_lab2(
    #     "kroA: ILS",
    #     kroa200_matrix,
    #     kroa200_coords,
    #     kroa200_cycle1_random,
    #     kroa200_cycle2_random,
    #     ils_wrapper
    # )

    # utils.run_test_lab2(
    #     "kroB: ILS",
    #     krob200_matrix,
    #     krob200_coords,
    #     krob200_cycle1_random,
    #     krob200_cycle2_random,
    #     ils_wrapper
    # )