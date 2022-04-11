#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-backports.entry_points_selectable
Version  : 1.1.1
Release  : 15
URL      : https://files.pythonhosted.org/packages/71/16/edd003270daaab0168f7dbac6e22b055322e9ba66fb2cc951f58d1ed158b/backports.entry_points_selectable-1.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/71/16/edd003270daaab0168f7dbac6e22b055322e9ba66fb2cc951f58d1ed158b/backports.entry_points_selectable-1.1.1.tar.gz
Summary  : Compatibility shim providing selectable entry points for older implementations
Group    : Development/Tools
License  : MIT
Requires: pypi-backports.entry_points_selectable-license = %{version}-%{release}
Requires: pypi-backports.entry_points_selectable-python = %{version}-%{release}
Requires: pypi-backports.entry_points_selectable-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: https://img.shields.io/pypi/v/backports.entry_points_selectable.svg
:target: `PyPI link`_

%package license
Summary: license components for the pypi-backports.entry_points_selectable package.
Group: Default

%description license
license components for the pypi-backports.entry_points_selectable package.


%package python
Summary: python components for the pypi-backports.entry_points_selectable package.
Group: Default
Requires: pypi-backports.entry_points_selectable-python3 = %{version}-%{release}

%description python
python components for the pypi-backports.entry_points_selectable package.


%package python3
Summary: python3 components for the pypi-backports.entry_points_selectable package.
Group: Default
Requires: python3-core
Provides: pypi(backports.entry_points_selectable)

%description python3
python3 components for the pypi-backports.entry_points_selectable package.


%prep
%setup -q -n backports.entry_points_selectable-1.1.1
cd %{_builddir}/backports.entry_points_selectable-1.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649717292
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-backports.entry_points_selectable
cp %{_builddir}/backports.entry_points_selectable-1.1.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-backports.entry_points_selectable/8e6689d37f82d5617b7f7f7232c94024d41066d1
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/backports/__init__.py
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/backports/__pycache__/__init__.cpython-3*.pyc

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-backports.entry_points_selectable/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
