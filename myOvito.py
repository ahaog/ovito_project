from ovito.io import import_file
from ovito.modifiers import *
from ovito.vis import Viewport
from ovito.vis import ParticlesVis
from ovito.qt_compat import QtCore
from ovito.qt_compat import QtGui
from ovito.vis import *
import math


def ovitoMain1():
    MaxX = 0
    MinX = 0
    MaxY = 0
    MinY = 0
    MaxZ = 0
    MinZ = 0

    pipeline = import_file("wire_melt_500000.dump")
    pipeline.add_to_scene()
    pipeline.modifiers.append(ExpressionSelectionModifier(expression='melted == 0'))
    pipeline.modifiers.append(DeleteSelectedModifier())
    data = pipeline.compute()
    vis_element = pipeline.source.data.particles.vis
    vis_element.shape = ParticlesVis.Shape.Square
    vis_element.radius = 0.0001

    # bar_length = 40
    # bar_color = QtGui.QColor(0, 0, 0)
    # label_text = f"{bar_length / 10} nm"
    # label_color = QtGui.QColor(255, 255, 255)

    # def render(args):
    #     if args.is_perspective:
    #         raise Exception("This overlay only works with non-perspective viewports.")
    #
    #     # Compute length of bar in screen space
    #     screen_length = args.project_size((0, 0, 0), bar_length)
    #
    #     # Define geometry of bar in screen space
    #     height = 0.07 * args.painter.window().height()
    #     margin = 0.02 * args.painter.window().height()
    #     rect = QtCore.QRectF(margin, margin, screen_length, height)
    #
    #     # Render bar rectangle
    #     args.painter.fillRect(rect, bar_color)
    #
    #     # Render text label
    #     font = args.painter.font()
    #     font.setPixelSize(height)
    #     args.painter.setFont(font)
    #     args.painter.setPen(QtGui.QPen(label_color))
    #     args.painter.drawText(rect, QtCore.Qt.AlignCenter, label_text)
    # render("wire_melt_500000.dump")

    # pos_property = data.particles.positions
    # l1 = []
    # for pos in pos_property:
    #     l1.append(pos[2])
    #
    # a = max(l1)
    # b = min(l1)
    # sr = (a - b) / 2
    # c = b + sr
    # print(c)

    # print(f"Длина : {(MaxX - MinX)}")
    # print(f"Высота : {(MaxY - MinY)}")
    # print(f"Ширина : {(MaxZ - MinZ)}")
    #
    # slice_mod = SliceModifier(distance=0.01, normal=(1, 0, 0))
    # pipeline.modifiers.append(slice_mod)
    # data = pipeline.compute()
    vp = Viewport()
    vp = Viewport(type=Viewport.Type.Ortho)
    tripod = CoordinateTripodOverlay(size=0.05)
    vp.overlays.append(tripod)
    # vp.type = Viewport.Type.Ortho
    vp.fov = 0.0074746
    vp.camera_pos = (0.0110289, 0, 0.00554922)
    vp.camera_dir = (0, 1, 0)
    # vp.fov = math.radians(60.0)
    vp.render_image(size=(1600, 1200), filename="figure.png", background=(1, 1, 1), frame=1)

    # Create a viewport:
    # viewport = Viewport(type=Viewport.Type.Top)
    #
    # # The user-defined function that will paint on top of rendered images:
    # def render_some_text(args: PythonViewportOverlay.Arguments):
    #     args.painter.drawText(10, 10, "Hello world")
    #
    # # Attach overlay function to viewport:
    # viewport.overlays.append(PythonViewportOverlay(function=render_some_text))

    # bar_length = 40
    # bar_color = QtGui.QColor(0, 0, 0)
    # label_text = f"{bar_length / 10} nm"
    # label_color = QtGui.QColor(255, 255, 255)
    #
    # def render(args):
    #     if args.is_perspective:
    #         raise Exception("This overlay only works with non-perspective viewports.")
    #
    #     # Compute length of bar in screen space
    #     screen_length = args.project_size((0, 0, 0), bar_length)
    #
    #     # Define geometry of bar in screen space
    #     height = 0.07 * args.painter.window().height()
    #     margin = 0.02 * args.painter.window().height()
    #     rect = QtCore.QRectF(margin, margin, screen_length, height)
    #
    #     # Render bar rectangle
    #     args.painter.fillRect(rect, bar_color)
    #
    #     # Render text label
    #     font = args.painter.font()
    #     font.setPixelSize(height)
    #     args.painter.setFont(font)
    #     args.painter.setPen(QtGui.QPen(label_color))
    #     args.painter.drawText(rect, QtCore.Qt.AlignCenter, label_text)
    # render(args=PythonViewportOverlay.Arguments)


ovitoMain1()
