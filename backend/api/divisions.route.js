import express from "express"
import DivisionsCtrl from "./divisions.controller.js"
// import ReviewsCtrl from "./reviews.controller.js"

const router = express.Router()

router.route("/").get(DivisionsCtrl.apiGetDivisions)
router.route("/id/:id").get(DivisionsCtrl.apiGetDivisionById)
// router.route("/cuisines").get(DivisionsCtrl.apiGetDivisionCuisines)

// router
//   .route("/review")
//   .post(ReviewsCtrl.apiPostReview)
//   .put(ReviewsCtrl.apiUpdateReview)
//   .delete(ReviewsCtrl.apiDeleteReview)

export default router
