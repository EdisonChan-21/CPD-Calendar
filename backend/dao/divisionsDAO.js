import mongodb from "mongodb"
const ObjectId = mongodb.ObjectID
let divisions

export default class DivisionsDAO {
  static async injectDB(conn) {
    if (divisions) {
      return
    }
    try {
      divisions = await conn.db(process.env.DIVISIONS_NS).collection("division")
    } catch (e) {
      console.error(
        `Unable to establish a collection handle in divisionsDAO: ${e}`,
      )
    }
  }

  static async getDivisions({
    filters = null,
    page = 0,
    divisionsPerPage = 20,
  } = {}) {
    let query
    if (filters) {
      if ("divisionName" in filters) {
        query = { $text: { $search: filters["divisionName"] } }
      } else if ("divisionUrl" in filters) {
        query = { "divisionUrl": { $eq: filters["divisionUrl"] } }
      }
    }

    let cursor

    try {
      cursor = await divisions
        .find(query)
    } catch (e) {
      console.error(`Unable to issue find command, ${e}`)
      return { divisionsList: [], totalNumDivisions: 0 }
    }

    const displayCursor = cursor.limit(divisionsPerPage).skip(divisionsPerPage * page)

    try {
      const divisionsList = await displayCursor.toArray()
      const totalNumDivisions = await divisions.countDocuments(query)

      return { divisionsList, totalNumDivisions }
    } catch (e) {
      console.error(
        `Unable to convert cursor to array or problem counting documents, ${e}`,
      )
      return { divisionsList: [], totalNumDivisions: 0 }
    }
  }
  static async getDivisionByID(id) {
    try {
      const pipeline = [
        {
            $match: {
                _id: new ObjectId(id),
            },
        },
              {
                  $lookup: {
                      from: "reviews",
                      let: {
                          id: "$_id",
                      },
                      pipeline: [
                          {
                              $match: {
                                  $expr: {
                                      $eq: ["$restaurant_id", "$$id"],
                                  },
                              },
                          },
                          {
                              $sort: {
                                  date: -1,
                              },
                          },
                      ],
                      as: "reviews",
                  },
              },
              {
                  $addFields: {
                      reviews: "$reviews",
                  },
              },
          ]
      return await divisions.aggregate(pipeline).next()
    } catch (e) {
      console.error(`Something went wrong in getRestaurantByID: ${e}`)
      throw e
    }
  }
  //
  // static async getCuisines() {
  //   let cuisines = []
  //   try {
  //     cuisines = await divisions.distinct("cuisine")
  //     return cuisines
  //   } catch (e) {
  //     console.error(`Unable to get cuisines, ${e}`)
  //     return cuisines
  //   }
  // }
}
