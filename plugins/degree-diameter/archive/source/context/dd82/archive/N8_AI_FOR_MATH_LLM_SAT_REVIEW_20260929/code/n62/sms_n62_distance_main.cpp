// Problem-specific SMS entry point for the rooted d=8, n=62 search.
//
// The base CNF handles degrees and all C--L constraints.  This propagator
// handles the expensive L--L distance-two disjunction without one Tseitin
// witness variable for every (x,y,z) triple.

#include "options.hpp"
#include "sms.hpp"

#include <boost/program_options.hpp>
#include <cstdlib>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace po = boost::program_options;

class N62DistanceTwoChecker : public PartiallyDefinedGraphChecker
{
  std::vector<unsigned> parent_masks;

public:
  N62DistanceTwoChecker(std::vector<unsigned> masks, int frequency)
      : PartiallyDefinedGraphChecker(frequency), parent_masks(std::move(masks))
  {
    name = "N62DistanceTwoChecker";
    checkFinal = true;
    if (parent_masks.size() != 53)
      throw std::runtime_error("N62_PARENT_MASKS must contain 53 values");
  }

  void checkProperty(const adjacency_matrix_t &matrix) override
  {
    const int n = static_cast<int>(matrix.size());
    if (n != 53)
      throw std::runtime_error("the n=62 checker expects a 53-vertex D graph");

    for (int x = 0; x < n; ++x)
      for (int y = x + 1; y < n; ++y)
      {
        if (parent_masks[x] & parent_masks[y])
          continue;
        if (matrix[x][y] != truth_value_false)
          continue;

        forbidden_graph_t reason;
        reason.push_back({truth_value_false, {x, y}});
        bool possible_witness = false;
        for (int z = 0; z < n; ++z)
        {
          if (z == x || z == y)
            continue;
          const truth_value_t xz = matrix[x][z];
          const truth_value_t yz = matrix[y][z];
          if (xz != truth_value_false && yz != truth_value_false)
          {
            possible_witness = true;
            break;
          }
          if (xz == truth_value_false)
            reason.push_back({truth_value_false, {std::min(x, z), std::max(x, z)}});
          else
            reason.push_back({truth_value_false, {std::min(y, z), std::max(y, z)}});
        }
        if (!possible_witness)
          throw reason;
      }
  }
};

static std::vector<unsigned> parse_parent_masks()
{
  const char *raw = std::getenv("N62_PARENT_MASKS");
  if (!raw)
    throw std::runtime_error("N62_PARENT_MASKS is not set");
  std::vector<unsigned> masks;
  std::stringstream stream(raw);
  std::string token;
  while (std::getline(stream, token, ','))
  {
    if (!token.empty())
      masks.push_back(static_cast<unsigned>(std::stoul(token)));
  }
  return masks;
}

int main(int argc, char const **argv)
{
  po::variables_map variables;
  GraphSolver *solver = parseOptions(argc, argv, variables);
  int frequency = 10;
  if (const char *raw = std::getenv("N62_PROP_FREQUENCY"))
    frequency = std::max(1, std::stoi(raw));
  solver->addPartiallyDefinedGraphChecker(
      new N62DistanceTwoChecker(parse_parent_masks(), frequency));
  const int result = solver->sms_solve();
  delete solver;
  return result;
}
