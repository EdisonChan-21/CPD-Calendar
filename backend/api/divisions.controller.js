import DivisionsDAO from "../dao/divisionsDAO.js"

export default class DivisionsController {
  static async apiGetDivisions(req, res, next) {
    const divisionsPerPage = req.query.divisionsPerPage ? parseInt(req.query.divisionsPerPage, 10) : 2
    const page = req.query.page ? parseInt(req.query.page, 10) : 0

    let filters = {}
    if (req.query.divisionName) {
      filters.divisionName = req.query.divisionName
    } else if (req.query.zipcode) {
      filters.divisionUrl = req.query.divisionUrl
    }

    const { divisionsList, totalNumDivisions } = await DivisionsDAO.getDivisions({
      filters,
      page,
      divisionsPerPage,
    })

    let response = {
      divisions: divisionsList,
      page: page,
      filters: filters,
      entries_per_page: divisionsPerPage,
      total_results: totalNumDivisions,
    }
    res.json(response)
  }
  static async apiGetDivisionById(req, res, next) {
    try {
      let id = req.params.id || {}
      let division = await DivisionsDAO.getDivisionByID(id)
      if (!division) {
        res.status(404).json({ error: "Not found" })
        return
      }
      res.json(division)
    } catch (e) {
      console.log(`api, ${e}`)
      res.status(500).json({ error: e })
    }
  }

  // static async apiGetdivisionCuisines(req, res, next) {
  //   try {
  //     let cuisines = await DivisionsDAO.getCuisines()
  //     res.json(cuisines)
  //   } catch (e) {
  //     console.log(`api, ${e}`)
  //     res.status(500).json({ error: e })
  //   }
  // }
}
