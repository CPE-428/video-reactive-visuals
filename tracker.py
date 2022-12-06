import cv2
import numpy as np


def detect_body(frame):
    # Convert BGR to gray
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blur = cv2.GaussianBlur(frame, (5, 5), 1)

    # Apply Canny edge detection
    edges = cv2.Canny(image=blur, threshold1=40, threshold2=50)
    return edges


def head_pose_w_dlib(frame):
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hog_face_detector = dlib.get_frontal_face_detector()

    # optional parameter - if face size smaller than 8×80, upsample image (increases resolution of image)
    results = hog_face_detector(frameRGB)
    for bbox in results:
        x1, y1, x2, y2 = bbox.left(), bbox.top(), bbox.right(), bbox.bottom()
        cv2.rectangle(frame, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=5)


def rect_to_bounding_box(rect):
    # converts dlib format to opencv format
    x, y = rect.left(), rect.top()
    w, h = rect.right() - x, rect.bottom() - y
    return (x, y, w, h)


def shape_to_np(shape, num_of_points=81, dtype="int"):
    coordinates = np.zeros((num_of_points, 2), dtype=dtype)
    for i in range(num_of_points):
        coordinates[i] = (shape.part(i).x, shape.part(i).y)

    return coordinates


# def head_pose(frame, shape_predictor):
#     im = cv2.imread("headPose (2).jpg")
#     size = im.shape
#
#     # TODO: FILL IN WITH DATA GATHERED WITH DLIB FACIAL LANDMARK DETECTION
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # detector = dlib.get_frontal_face_detector()
#     # predictor = dlib.shape_predictor(shape_predictor)
#
#     # detects faces
#     # faces = detector(gray, 1)
#
#     for (i, face) in enumerate(faces):
#         # determine facial landmarks and convert to numpy array
#         # shape = predictor(gray, face)
#         shape = shape_to_np(shape)
#
#         # draw bounding box around face
#         (x, y, w, h) = rect_to_bounding_box(face)
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#         # draw facial landmarks on image
#         for (x, y) in shape:
#             cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
#
#     # 2D image points. If you change the image, you need to change vector
#     image_points = np.array([
#         (359, 391),  # Nose tip
#         (399, 561),  # Chin
#         (337, 297),  # Left eye left corner
#         (513, 301),  # Right eye right corne
#         (345, 465),  # Left Mouth corner
#         (453, 469)  # Right mouth corner
#     ], dtype="double")
#
#     # 3D model points. APPROXIMATE 3D MODEL OF A FACE:
#     model_points = np.array([
#         (0.0, 0.0, 0.0),  # Nose tip
#         (0.0, -330.0, -65.0),  # Chin
#         (-225.0, 170.0, -135.0),  # Left eye left corner
#         (225.0, 170.0, -135.0),  # Right eye right corne
#         (-150.0, -150.0, -125.0),  # Left Mouth corner
#         (150.0, -150.0, -125.0)  # Right mouth corner
#
#     ])
#
#     # Camera internals
#
#     focal_length = size[1]
#     center = (size[1] / 2, size[0] / 2)
#     camera_matrix = np.array(
#         [[focal_length, 0, center[0]],
#          [0, focal_length, center[1]],
#          [0, 0, 1]], dtype="double"
#     )
#
#     print("Camera Matrix :\n {0}".format(camera_matrix))
#
#     dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion
#     (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix,
#                                                                   dist_coeffs,
#                                                                   flags=cv2.SOLVEPNP_ITERATIVE)
#
#     print("Rotation Vector:\n {0}".format(rotation_vector))
#     print("Translation Vector:\n {0}".format(translation_vector))
#
#     # Project a 3D point (0, 0, 1000.0) onto the image plane.
#     # We use this to draw a line sticking out of the nose
#
#     (nose_end_point2D, jacobian) = cv2.projectPoints(np.array([(0.0, 0.0, 1000.0)]), rotation_vector,
#                                                      translation_vector,
#                                                      camera_matrix, dist_coeffs)
#
#     for p in image_points:
#         cv2.circle(im, (int(p[0]), int(p[1])), 3, (0, 0, 255), -1)
#
#     p1 = (int(image_points[0][0]), int(image_points[0][1]))
#     p2 = (int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))
#
#     print(p1, p2)
#     cv2.line(im, p1, p2, (255, 0, 0), 2)
#
#     # Display image
#     cv2.imshow("Output", im)
#     cv2.waitKey(0)
